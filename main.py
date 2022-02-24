# 事前に pip install "gql[all]" を行なってください
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

transport = AIOHTTPTransport(url="https://api.obniz.com/v1/graphql")
client = Client(transport=transport, fetch_schema_from_transport=True)

query = gql(
    """
{
  devices(first: 1) {
    totalCount
    pageInfo {
      hasNextPage
      hasPreviousPage
    }
    edges {
      node {
        id
        access_token
        description
        metadata
        devicekey
        hardware
        os
        osVersion
        region
        status
        pingInterval
        createdAt
        deviceLiveInfo {
          isOnline
          connectedNetwork {
            online_at
            net
            local_ip
            global_ip
            wifi {
              ssid
              macAddress
              rssi
            }
            wifimesh {
              parent_obniz_id
              root_obniz_id
            }
          }
        }
        user {
          id
        }
        configs
      }
    }
  }
}
"""
)


if __name__ == '__main__':
    result = client.execute(query)
    print(result)
