from email import message
import hmac
import hashlib
from inspect import signature
from urllib.parse import parse_qsl
from app.core.config import settings

def verify_shopify_signature(query_params: dict) -> bool:
    """
    Verifies the signature from a Shopify App Proxy request.
    Shopify sends 'signature' and other params. We must hash the other params
    and compare with the provided signature.
    """
    if "signature" not in query_params:
        return False

    received_signature = query_params["signature"]

    # Sort and prepare parameters for hashing (exclude signature)
    params = dict(query_params)
    del params["signature"]
    sorted_params = "".join([f"{k}={params[k]}" for k in sorted(params.keys())])

    # Calculate HMAC SHA256
    secret = settings.SHOPIFY_API_SECRET.encode("utf-8")
    message = sorted_params.encode("utf-8")
    calculated_signature = hmac.new(secret, message, hashlib.sha256).hexdigest()

    return hmac.compare_digest(received_signature, calculated_signature)