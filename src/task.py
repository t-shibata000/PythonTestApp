from pydantic import BaseModel

class Task(BaseModel):
    id: int
    title: str
    time: int
    start_time: str
    end_time: str
    def set_id(self, id):
        self.id=id
    def set_start_time(self, s_time):
        self.start_time=s_time
    def set_end_time(self, e_time):
        self.end_time=e_time