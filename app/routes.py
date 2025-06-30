from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.models import *
from flask_mail import Mail, Message
from app import mail


main = Blueprint("main", __name__)



@main.route('/')
def home():
    rooms = Room.query.all()
    return render_template('index.html', rooms=rooms)



@main.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        room = Room(
            room_number=request.form['room_number'],
            is_available=(request.form['status'] == 'available'),
            rent=request.form['rent'],
            admin_email=request.form['admin_email'],
            admin_phone=request.form['admin_phone']
        )
        db.session.add(room)
        db.session.commit()
        flash("Room added/updated successfully!", "success")
    rooms = Room.query.all()
    return render_template('admin.html', rooms=rooms)



@main.route('/book/<int:room_id>', methods=['GET', 'POST'])
def book(room_id):
    room = Room.query.get_or_404(room_id)
    if request.method == 'POST':
        booking = BookingRequest(
            room_id=room_id,
            name=request.form['name'],
            email=request.form['email'],
            phone=request.form['phone'],
            message=request.form['message']
        )
        db.session.add(booking)
        db.session.commit()

        msg = Message("New Room Booking Request",
                      sender='your_email@gmail.com',
                      recipients=[room.admin_email])
        msg.body = f"New request for Room {room.room_number}\n\nName: {booking.name}\nEmail: {booking.email}\nPhone: {booking.phone}\nMessage: {booking.message}"
        mail.send(msg)
        flash("Booking request sent to admin!", "success")
        return redirect(url_for('main.home'))
    return render_template('book.html', room=room)










