from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user
import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DecimalField, IntegerField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from flask_babel import _, lazy_gettext as _l
from werkzeug.datastructures import MultiDict
from decimal import Decimal

from .models.product_summary import ProductSummary
from .models.purchase import Purchase
from .models.product_sellers import ProductSeller
from .models.product import Product

from app.models import Carts
from .models.Carts import Cartesian
from .models.user import User
from .models.product_summary import ProductSummary
from .models.generic_queries import *
from .models.messages import *


from flask import Blueprint
bp = Blueprint('Cart', __name__)

class placeOrder(FlaskForm):
    confirm = SelectField(_l('Confirm'), choices = [(1,"Check Discount Code"),(2,"Confirm Purchase")],validators=[DataRequired()])
    address = StringField(_l('Address'), validators=[DataRequired()])
    code = StringField(_l('Discount Code'))
    submit = SubmitField(_l('Place Order'))

@bp.route('/myCart',methods=['GET', 'POST'])
def myCart():
    form11 = placeOrder()
    if request.method == 'GET':
       form11= placeOrder(formdata = MultiDict({
            'address': current_user.address,
        }))
    empty = False
    unread = None
    if current_user.is_authenticated:
        unread = num_unread()
        balance = User.get(current_user.id).balance
        totalcost = 0
        ido = Cartesian.get(current_user.id)
        save_for_later = Cartesian.getSaved(current_user.id)
        if save_for_later is None:
            any_saved = False 
        else:
            any_saved = True
        if ido is None:
            empty = True
            return render_template('myCart.html',
                            unread = unread,
                            form = form11,
                            currcart = ido,
                            empty = empty,
                            balance = balance,
                            saved = save_for_later,
                            any_saved = any_saved,
                            savings = 0,
                            )
        """
        if dform.validate_on_submit and good_code(dform.code.data):
            DiscountCode = dform.code.data
            usersCode.dCode = dform.code.data
            redirect(url_for('Cart.myCart', dcode = dform.code.data))
        elif good_code(dform.code.data):
             DiscountCode = dform.code.data
        else:
            DiscountCode = "No Code"
            usersCode.dCode = "No Code"
        """
        #products = []
        #for item in ido:
        #    products.append([0, item.pid, item.quantity, item.price])
        #SELECT Users.firstname, Products.pid, CARTS.quantity, Products.price
        products = ido
        savings = 0
        for product in ido:
            if form11.code.data != "No Code" and good_code(form11.code.data):
                product.price, item_savings = discount(form11.code.data, product.pid, product.price)
                savings += item_savings*product.quantity
            totalcost += Decimal(product.price* product.quantity)
        hasEnough = True
        total = totalcost
        if balance < totalcost:
            hasEnough = False
        if form11.validate_on_submit:
            if form11.confirm.data == '2' and hasEnough:
                albert = Cartesian.placeOrder(current_user.id, form11.address.data)
                if User.update_balance(current_user.id,
                                   int(balance),
                                   total,
                                   "wdr"):
                    flash('Your balance has been updated!')
                    for product in products:
                        seller = who_sells(product.pid)
                        balance = User.get(seller).balance
                        User.update_balance(seller, int(balance), product.price * product.quantity, "dep")
                for product in ido:
                    #print(gangarang.price)
                    Cartesian.addtoOrder(albert,product.pid,product.quantity,product.price)
                    Product.adjustWithOrder(product.pid, product.quantity)
                    Cartesian.removeFromCart(product.pid,current_user.id)
                return redirect(url_for('BuyerOrders.buyer_orders', uid = current_user.id))
       
    return render_template('myCart.html',
                            unread=unread,
                            form = form11,
                            currcart = products,
                            empty = empty,
                            balance = balance,
                            totalcost=totalcost,
                            hasEnough=hasEnough,
                            saved = save_for_later,
                            any_saved = any_saved,
                            code = form11.code.data,
                            savings = savings)

@bp.route('/myCart/<uid>/<pid>/<quantity>',methods=['GET', 'POST'])
def saveForLater(uid, pid, quantity):
    save_for_later(uid, pid, quantity)
    return redirect(url_for('Cart.myCart'))

@bp.route('/myCart/delete/<uid>/<pid>',methods=['GET', 'POST'])
def deleteSaved(uid, pid):
    delete_saved(uid, pid)
    return redirect(url_for('Cart.myCart'))

@bp.route('/myCart/add/<uid>/<pid>/<quantity>',methods=['GET', 'POST'])
def addCart(uid, pid, quantity):
    back_in_cart(uid, pid, quantity)
    return redirect(url_for('Cart.myCart'))