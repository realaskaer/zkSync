from modules import Logger, Aggregator
from settings import INSCRIPTION_DATA
from utils.tools import helper


class Inscription(Logger, Aggregator):
    def __init__(self, client):
        Logger.__init__(self)
        Aggregator.__init__(self, client)
        self.stop_flag = False
        self.signed_tx = None

    async def swap(self):
        pass

    @helper
    async def mint_inscribe(self):
        tx_params = (await self.client.prepare_transaction()) | {
            'data': INSCRIPTION_DATA.encode(),
            'to': self.client.address
        }

        return await self.client.send_transaction(tx_params)
