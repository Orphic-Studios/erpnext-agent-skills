"""
Frappe & ERPNext v15 REST API Client Tool
Compatible with Python 3.9+ and Frappe Framework v15 REST conventions.
Provides synchronous and structured methods for Advisory & Executive Agent Workflows.
"""

from __future__ import annotations
import json
import os
import urllib.parse
from typing import Any, Dict, List, Optional, Union
import requests


class FrappeAPIException(Exception):
    """Custom exception encapsulating Frappe v15 REST errors."""
    def __init__(self, status_code: int, message: str, server_messages: Optional[str] = None):
        super().__init__(f"HTTP {status_code}: {message}")
        self.status_code = status_code
        self.message = message
        self.server_messages = server_messages


class FrappeClient:
    """
    Standardized Client for Frappe/ERPNext v15 API interactions.
    Supports Token Auth (token <api_key>:<api_secret>) and Basic Session headers.
    """

    def __init__(
        self,
        base_url: Optional[str] = None,
        api_key: Optional[str] = None,
        api_secret: Optional[str] = None,
        timeout: int = 30,
    ):
        self.base_url = (base_url or os.getenv("FRAPPE_BASE_URL", "http://localhost:8000")).rstrip("/")
        self.api_key = api_key or os.getenv("FRAPPE_API_KEY")
        self.api_secret = api_secret or os.getenv("FRAPPE_API_SECRET")
        self.timeout = timeout
        self.session = requests.Session()

        if self.api_key and self.api_secret:
            self.session.headers.update({
                "Authorization": f"token {self.api_key}:{self.api_secret}",
                "Accept": "application/json",
                "Content-Type": "application/json",
            })

    def _handle_response(self, response: requests.Response) -> Any:
        try:
            data = response.json()
        except Exception:
            data = {"message": response.text}

        if not response.ok:
            server_msgs = None
            if "_server_messages" in data:
                try:
                    msgs = json.loads(data["_server_messages"])
                    server_msgs = "; ".join([json.loads(m).get("message", "") for m in msgs])
                except Exception:
                    server_msgs = data.get("_server_messages")

            exc_msg = server_msgs or data.get("exception") or data.get("message") or response.reason
            raise FrappeAPIException(response.status_code, str(exc_msg), server_messages=server_msgs)

        if "data" in data:
            return data["data"]
        elif "message" in data:
            return data["message"]
        return data

    def get_list(
        self,
        doctype: str,
        filters: Optional[Union[Dict[str, Any], List[List[Any]]]] = None,
        fields: Optional[List[str]] = None,
        order_by: Optional[str] = None,
        limit_start: int = 0,
        limit_page_length: int = 20,
    ) -> List[Dict[str, Any]]:
        """Retrieve list of documents with filtering, projection, and pagination."""
        params: Dict[str, Any] = {
            "limit_start": limit_start,
            "limit_page_length": limit_page_length,
        }
        if filters:
            params["filters"] = json.dumps(filters)
        if fields:
            params["fields"] = json.dumps(fields)
        if order_by:
            params["order_by"] = order_by

        url = f"{self.base_url}/api/resource/{urllib.parse.quote(doctype)}"
        res = self.session.get(url, params=params, timeout=self.timeout)
        return self._handle_response(res)

    def get_doc(self, doctype: str, name: str) -> Dict[str, Any]:
        """Fetch a single document by DocType and primary name ID."""
        url = f"{self.base_url}/api/resource/{urllib.parse.quote(doctype)}/{urllib.parse.quote(name)}"
        res = self.session.get(url, timeout=self.timeout)
        return self._handle_response(res)

    def create_doc(self, doctype: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new document in ERPNext (Initial state: Draft docstatus=0)."""
        url = f"{self.base_url}/api/resource/{urllib.parse.quote(doctype)}"
        res = self.session.post(url, json=data, timeout=self.timeout)
        return self._handle_response(res)

    def update_doc(self, doctype: str, name: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Update fields of an existing document."""
        url = f"{self.base_url}/api/resource/{urllib.parse.quote(doctype)}/{urllib.parse.quote(name)}"
        res = self.session.put(url, json=data, timeout=self.timeout)
        return self._handle_response(res)

    def delete_doc(self, doctype: str, name: str) -> Dict[str, Any]:
        """Delete an existing draft/cancelled document."""
        url = f"{self.base_url}/api/resource/{urllib.parse.quote(doctype)}/{urllib.parse.quote(name)}"
        res = self.session.delete(url, timeout=self.timeout)
        return self._handle_response(res)

    def submit_doc(self, doctype: str, name: str) -> Dict[str, Any]:
        """Submit a submittable document (docstatus = 1) using standard Frappe method."""
        return self.call_method("frappe.client.submit", doc={"doctype": doctype, "name": name})

    def cancel_doc(self, doctype: str, name: str) -> Dict[str, Any]:
        """Cancel a submitted document (docstatus = 2) using standard Frappe method."""
        return self.call_method("frappe.client.cancel", doctype=doctype, name=name)

    def call_method(self, method: str, **kwargs) -> Any:
        """Call any whitelisted Python method via RPC."""
        url = f"{self.base_url}/api/method/{method}"
        res = self.session.post(url, json=kwargs, timeout=self.timeout)
        return self._handle_response(res)
