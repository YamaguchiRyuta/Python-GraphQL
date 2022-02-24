# 事前に pip install "gql[all]" を行なってください
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

transport = AIOHTTPTransport(url="https://api.obniz.com/v1/graphql")
client = Client(transport=transport, fetch_schema_from_transport=True)

query = gql(
    """
    query getContinents {
      continents {
        code
        name
      }
    }
"""
)


if __name__ == '__main__':
    result = client.execute(query)
    print(result)
