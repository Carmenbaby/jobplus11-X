from flask import Blueprint, render_template, redirect, url_for, flash
from jobplus.form import CompanyProfileForm
from flask_login import login_required, current_user

company = Blueprint('company', __name__,url_prefix='/company')

@company.route('/profile/', methods=['GET', 'POST'])
@login_required
def profile():
    if not current_user.is_company:
        flash('非企业用户，无权限', 'warning')
        return redirect(url_for('front.index'))
    form = CompanyProfileForm(obj=current_user.company_detail)
    form.name.data = current_user.name
    form.email.data = current_user.email
    if current_user.phone:#这里要是不判断的话，validate_phone时候会报错。
        form.phone.data = current_user.phone

    if form.validate_on_submit():
        form.updated_profile(current_user)
        flash('企业信息更新成功', 'success')
        return redirect(url_for('front.index'))
    return render_template('company/profile.html', form=form)