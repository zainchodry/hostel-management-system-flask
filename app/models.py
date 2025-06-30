from app.extensions import db


class Room(db.Model):
    __tablename__ = "room"
    id = db.Column(db.Integer, primary_key = True)
    room_number = db.Column(db.String(10), nullable = False)
    is_available = db.Column(db.Boolean, default = True)
    rent = db.Column(db.Integer)
    admin_email = db.Column(db.String(100))
    admin_phone = db.Column(db.String(20))

    def __repr__(self) -> str:
        return f"{self.admin_email} - {self.admin_phone}"


class BookingRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    message = db.Column(db.Text)

    def __repr__(self) -> str:
        return f"{self.name} - {self.email} - {self.phone}"
    


