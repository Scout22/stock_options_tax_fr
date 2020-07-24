#!/usr/bin/env python3
# coding: utf-8

from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, FloatField

from wtforms import validators

from stock_option_calculator import compute_tax


class CalcForm(FlaskForm):
    stock_aquisition_price = FloatField("Prix d'aquisition de l'action",default=1.25)
    stock_qty = IntegerField("Nombre d'action", default=1650)
    stock_exercise_price = FloatField("Cours de l'action lors de la levée")
    stock_sell_price = FloatField("Cours de l'action lors de la vente")
    gain_before_tax = FloatField("Gain avant impot")
    tax = FloatField("Impot")
    gain_after_tax = FloatField("Gain net d'impot")
    submit = SubmitField("Valider")


app = Flask(__name__)
app.secret_key = 'development key'


@app.route('/', methods=['GET', 'POST'])
def calc():
    form = CalcForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            form.tax.data = compute_tax(form.stock_aquisition_price.data,0.20,form.stock_exercise_price.data,form.stock_sell_price.data, form.stock_qty.data)
            form.gain_before_tax.data = form.stock_sell_price.data - form.stock_aquisition_price.data
            form.gain_after_tax.data = form.gain_before_tax.data - form.tax.data

    return render_template('main_page.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
