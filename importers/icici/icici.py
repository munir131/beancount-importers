from beancount.ingest.importers import csv
from beancount.ingest.importers.csv import Col
import re
from os import path
import logging


logger = logging.getLogger(__name__)



class IciciBankImporter(csv.Importer):

    config = {Col.DATE: 'Value Date',
            Col.PAYEE: 'Transaction Remarks',
            Col.AMOUNT_DEBIT: 'Withdrawal Amount (INR )',
            Col.AMOUNT_CREDIT: 'Deposit Amount (INR )',
            Col.BALANCE: 'Balance (INR )'}

    def __init__(self, base_account='Assets:IN:Bank:ICICI:Savings'):
      super().__init__(
        self.config,
        base_account,
        'INR', 
        )