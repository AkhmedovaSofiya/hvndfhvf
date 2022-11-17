from flask import Flask, render_template, redirect, request
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

app = Flask(__name__, static_folder='/')


@app.route("/", methods=["GET", "POST"])
def main():
    return redirect('/about')


@app.route("/about", methods=["GET", "POST"])
def about():
    return render_template('about.html')


@app.route("/contact", methods=["GET", 'POST'])
def contact():
    if request.method == 'GET':
        return render_template('contact.html')
    elif request.method == 'POST':
        name = request.form.get('name')
        mail = request.form.get('email')
        contact = request.form.get('contact')
        message = request.form.get('message')

        fromaddr = "personal_website@mail.ru"
        toaddr = "gartman1969@list.ru"
        # mypass = "copsig-zaFsyz-mujra5"
        mypass = "NWaem5MMbv1c4LsFX2Ud"

        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = name

        body = f"""{mail}\n{contact}\n{message}"""
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
        server.login(fromaddr, mypass)
        server.sendmail(fromaddr, toaddr, text)
        return redirect('/')
    return redirect('/contact')


@app.route("/experience", methods=["GET"])
def experience():
    return render_template('experience.html')


@app.route("/portfolio", methods=["GET"])
def portfolio():
    return render_template('portfolio.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
