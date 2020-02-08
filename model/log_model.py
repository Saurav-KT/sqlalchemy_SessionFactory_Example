from sqlalchemy import Column, String, Date, Integer, Numeric
from common.base import Base
class log(Base):
    __tablename__ = 'tbl_log'
    __table_args__ = {'schema': 'DPS_Harmonization'}

    Id = Column(Integer, primary_key=True, mssql_identity_increment=1)
    log_description = Column(String)
    log_date = Column(Date)
    ip_address = Column(String)

    def __init__(self, log_description, log_date, ip_address):
        self.log_description = log_description
        self.log_date = log_date
        self.ip_address = ip_address
