from flask import Blueprint, render_template

import sqlaload as sl
from regenesis.core import app, engine, get_catalog
from regenesis.database import statistic_table

blueprint = Blueprint('statistic', __name__)

@blueprint.route('/<catalog>/statistics')
def index(catalog):
    catalog = get_catalog(catalog)
    statistics = sl.find(engine, statistic_table,
            order_by='title_de')
    return render_template('statistic/index.html',
            catalog=catalog,
            statistics=statistics)

@blueprint.route('/<catalog>/statistics/<name>')
def view(catalog, name):
    catalog = get_catalog(catalog)
    statistic = sl.find_one(engine, statistic_table, name=name)
    return render_template('statistic/view.html',
            catalog=catalog,
            statistic=statistic)




