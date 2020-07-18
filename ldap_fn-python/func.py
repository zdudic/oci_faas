import os
import sys
import io
import json
from fdk import response
 
def handler(ctx, data: io.BytesIO=None):
    """
    input is '{"compute" : "some oci compute"}', invoke function as:
    $ echo -n '{"ocicompute" : "some-oci-compute-fqdn"}' | fn -v invoke <app-name> <fn-name>
    """
    body = json.loads(data.getvalue())
    ocicompute = body["ocicompute"]
    resp = ldap_cfg(ocicompute)
    return response.Response(
        ctx,
        response_data=json.dumps(resp),
        headers={"Content-Type": "application/json"}
    )
 
# ----- my code
def ldap_cfg(ocicompute):
 
    opc_public_key="/home/fn/.ssh/id_rsa-opc"
    try:
        os.system('ssh -i %s -o "StrictHostKeyChecking no" opc@%s "sudo bash -s" < /function/ldap_config.sh >/dev/null' % (opc_public_key, ocicompute))
    except Exception as err:   # general exception
        sys.exit("Error: {0}".format(err))
     
    resp = ("LDAP is configured on " + ocicompute)
    return resp

