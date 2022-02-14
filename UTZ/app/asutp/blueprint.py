from flask import Blueprint, render_template, request, redirect, url_for, send_from_directory
from flask_security import login_required
from models import kii, events
#from .forms import PostForm, IsForm
#import ipaddress
from app import db
#from itertools import groupby
#from test_pd import test, invit_ipy


asutp = Blueprint('asutp', __name__, template_folder='templates')
            

@asutp.route('/asutp')
@login_required
def index():
    eve = events.query.all()
    return render_template('asutp/index.html', eve = eve)
    
    
@asutp.route('/<kiii>')
@login_required
def kii_detail(kiii):
    infa = kii.query.filter(kii.okii == str(kiii)).all()
    return render_template('asutp/kii_detail.html', infa = infa)

    

@asutp.route('/dowland/<okii>/<path:name>', methods = ['POST', 'GET'])
def dowland(name, okii):
    if (okii == "ТДП Уфа" or okii == "РДП Челябинск" or okii == "РДП Курган" or okii == "РДП Калтасы" or okii == "РДП Субханкулово" or okii == "РДП Нурлино") and name == "Акт категорирования":
        name1 = "Акт категорирования ЗОКИИ.pdf"
    elif name == "План реагирования на компьютерные инциденты":
        name1 = str(name) + " " + str(okii) + '.pdf'
    elif name == "Сведения":
        name1 = str(name) + " " + str(okii) + '.pdf'
    elif name == "Модель нарушителя":
        name1 = str(name) + " " + str(okii) + '.pdf'
    elif name == "Модель угроз":
        name1 = str(name) + " " + str(okii) + '.pdf'
    elif name == "оценка показателей":
        name1 = str(name) + " " + str(okii) + '.pdf'
    else:
        name1 = "Акт категорирования ОКИИ.pdf"
    directoryy = 'C:/Users/arpishkinmi/Desktop/UTZ/app/static/pdf/' + str(name) + '/'
    
    return send_from_directory(
            directory = directoryy, filename = name1, mimetype = 'application/pdf'
        )
        

    