from flask import Flask
from flask_login import LoginManager
from flask_babel import Babel
from .config import Config
from .db import DB


login = LoginManager()
login.login_view = 'users.login'
babel = Babel()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.db = DB(app)
    login.init_app(app)
    babel.init_app(app)

    from .users import bp as user_bp
    app.register_blueprint(user_bp)

    from .myaccount import bp as myaccount_bp
    app.register_blueprint(myaccount_bp)

    from .updatebalance import bp as updatebalance_bp
    app.register_blueprint(updatebalance_bp)
    
    from .product_summaries import bp as product_summary_bp
    app.register_blueprint(product_summary_bp)
    
    from .add_new_product import bp as add_new_product_bp
    app.register_blueprint(add_new_product_bp)

    from .seller import seller_inventory_bp as seller_inventory_bp
    app.register_blueprint(seller_inventory_bp)

    from .seller import seller_orders_bp as seller_orders_bp
    app.register_blueprint(seller_orders_bp)

    from .seller import seller_order_details_bp as seller_order_details_bp
    app.register_blueprint(seller_order_details_bp)

    from .seller import seller_product_fulfillment_bp as seller_product_fulfillment_bp
    app.register_blueprint(seller_product_fulfillment_bp)

    from .myCart import bp as cart_bp
    app.register_blueprint(cart_bp)

    from .productPage import bp as product_page_bp
    app.register_blueprint(product_page_bp)

    from .updateinformation import bp as update_infromation_bp
    app.register_blueprint(update_infromation_bp)    
    
    from .updatepassword import bp as update_password_bp
    app.register_blueprint(update_password_bp)

    from .updateproduct import bp as update_product_bp
    app.register_blueprint(update_product_bp)

    from .RemoveFromCart import bp as remove_From_Cart_bp
    app.register_blueprint(remove_From_Cart_bp)

    from .seller import seller_page_bp as seller_page_bp
    app.register_blueprint(seller_page_bp)

    from .messages import messages_bp as messages_bp
    app.register_blueprint(messages_bp)

    from .messages import message_details_bp as message_details_bp
    app.register_blueprint(message_details_bp)

    from .messages import messages_email_bp as message_email_bp
    app.register_blueprint(message_email_bp)

    from .social import bp as social_bp
    app.register_blueprint(social_bp)

    from .social import bp2 as social_bp_adv
    app.register_blueprint(social_bp_adv)

    from .buyer import buyer_bp as buyer_bp
    app.register_blueprint(buyer_bp)

    from .seeSpecificOrder import bp as sSO_bp
    app.register_blueprint(sSO_bp)

    from .seller import deletion_page_bp as delete_pr_bp
    app.register_blueprint(delete_pr_bp)

    from .seller import restore_bp as restore_bp
    app.register_blueprint(restore_bp)

    return app
