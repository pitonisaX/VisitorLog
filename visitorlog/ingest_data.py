
class VisitorList(Base):

__tablename__ = 'VisitorList'

id = Column(Integer, primary_key=True)
Visitor_name = Column(String)
Email = Column(String)
Phone = Column(String)
Visited_name = Column(String)
Date
Time_of_visit