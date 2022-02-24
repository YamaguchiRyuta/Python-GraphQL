# 事前に pip install "gql[all]" を行なってください (https://gql.readthedocs.io/en/latest/intro.html#less-dependencies)
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
from pprint import pprint

# https://obniz.com/ja/console/apikeys/ で生成したAPIキー
access_token = 'token_...'
# obnizクラウドAPIエンドポイント
url = 'https://api.obniz.com/v1/graphql'

# ----- 事前準備 -----
transport = AIOHTTPTransport(url=url, headers={'Authorization': f'Bearer {access_token}'})
client = Client(transport=transport)

# ----- 全件取得 -----
result = client.execute(gql("""
query {
  devices {
    edges {
      node { id access_token hardware os osVersion }
    }
  }
}"""))
pprint(result)
# {
#   'devices': {
#     'edges': [
#       {'node': {'id': '0000-0000', 'access_token': 'xxx', 'hardware': 'xxx', 'os': 'xxx', 'osVersion': '0.0.0'}}
#     ]
#   }
# }

# ----- ObnizIDを指定して１件取得 -----
result = client.execute(gql("""
query($obniz_id:String!) {
  devices(id: $obniz_id) {
    edges {
      node { id access_token hardware os osVersion }
    }
  }
}"""), variable_values={'obniz_id': '0000-0000'})
pprint(result)
