import werkzeug.exceptions
from flask import jsonify, request
from app.views import bp
from app.controllers.main_controller import *
from ressources import messages as m
from flask_cors import cross_origin
@bp.route('/')
@cross_origin()
def home():
    return jsonify(m.request_denied)

@bp.route('/get/users', methods=["POST"])
@cross_origin()
def get_user():
    data = request.json
    api_key = data.get("key")
    app_id = data.get("appid")
    if authenticate_app(api_key, app_id):
        try:
            filter = data.get("filter")
        except:
            filter = None
        users = get_users(filter)
        return jsonify(users)
    else:
        return jsonify(m.authentication_failed)

@bp.route('/insert/users', methods=["POST"])
@cross_origin()
def insert_users():
    data = request.json
    api_key = data.get("key")
    app_id = data.get("appid")
    if authenticate_app(api_key, app_id):
        new_user = {
            "firstName": data.get("firstName"),
            "lastName": data.get("lastName"),
            "role": data.get("role"),
            "password": data.get("password"),
            "email": data.get("email"),
            "category": data.get("category")
        }
        return insert_user(new_user)
    else:
        return jsonify(m.authentication_failed)

@bp.route('/update/users/<user_id>', methods=["PUT"])
@cross_origin()
def update_users(user_id):
    data = request.json
    api_key = data.get("key")
    app_id = data.get("appid")
    if authenticate_app(api_key, app_id):
        updated_user = {
            "firstName": data.get("firstName"),
            "lastName": data.get("lastName"),
            "role": data.get("role"),
            "password": data.get("password"),
            "email": data.get("email"),
            "category": data.get("category")
        }
        return update_user(user_id, updated_user)
    else:
        return jsonify(m.authentication_failed)

@bp.route('/remove/users/<user_id>', methods=["PUT"])
@cross_origin()
def remove_users(user_id):
    data = request.json
    api_key = data.get("key")
    app_id = data.get("appid")
    if authenticate_app(api_key, app_id):
        return delete_user(user_id)
    else:
        return jsonify(m.authentication_failed)
@bp.route('/get/groups', methods=["POST"])
@cross_origin()
def get_group():
    data = request.json
    api_key = data.get("key")
    app_id = data.get("appid")
    if authenticate_app(api_key, app_id):
        try:
            filter = data.get("filter")
        except:
            filter = None
        groups = get_groups(filter)
        return jsonify(groups)
    else:
        return jsonify(m.authentication_failed)

@bp.route('/insert/groups', methods=["POST"])
@cross_origin()
def insert_groups():
    data = request.json
    api_key = data.get("key")
    app_id = data.get("appid")
    if authenticate_app(api_key, app_id):
        new_group = {
            "name": data.get("name"),
            "description": data.get("description"),
            "category": data.get("category"),
            "points" : 0
        }
        return insert_group(new_group)
    else:
        return jsonify(m.authentication_failed)

@bp.route('/update/groups/<group_id>', methods=["PUT"])
@cross_origin()
def update_groups(group_id):
    data = request.json
    api_key = data.get("key")
    app_id = data.get("appid")
    if authenticate_app(api_key, app_id):
        updated_group = {
            "name": data.get("name"),
            "description": data.get("description"),
            "category": data.get("category")
        }
        return update_group(group_id, updated_group)
    else:
        return jsonify(m.authentication_failed)

@bp.route('/remove/groups/<group_id>', methods=["PUT"])
@cross_origin()
def remove_groups(group_id):
    data = request.json
    api_key = data.get("key")
    app_id = data.get("appid")
    if authenticate_app(api_key, app_id):
        return delete_group(group_id)
    else:
        return jsonify(m.authentication_failed)

@bp.route('/get/categories', methods=["POST"])
@cross_origin()
def get_category():
    data = request.json
    api_key = data.get("key")
    app_id = data.get("appid")
    if authenticate_app(api_key, app_id):
        try:
            filter = data.get("filter")
        except:
            filter = None
        categories = get_categories(filter)
        return jsonify(categories)
    else:
        return jsonify(m.authentication_failed)

@bp.route('/insert/categories', methods=["POST"])
@cross_origin()
def insert_categories():
    data = request.json
    api_key = data.get("key")
    app_id = data.get("appid")
    if authenticate_app(api_key, app_id):
        new_category = {
            "categoryName": data.get("name"),
        }
        return insert_category(new_category)
    else:
        return jsonify(m.authentication_failed)

@bp.route('/update/categories/<category_id>', methods=["PUT"])
@cross_origin()
def update_categories(category_id):
    data = request.json
    api_key = data.get("key")
    app_id = data.get("appid")
    if authenticate_app(api_key, app_id):
        updated_category = {
            "categoryName": data.get("name")
        }
        return update_category(category_id, updated_category)
    else:
        return jsonify(m.authentication_failed)

@bp.route('/remove/categories/<category_id>', methods=["PUT"])
@cross_origin()
def remove_categories(category_id):
    data = request.json
    api_key = data.get("key")
    app_id = data.get("appid")
    if authenticate_app(api_key, app_id):
        return delete_category(category_id)
    else:
        return jsonify(m.authentication_failed)

@bp.route('/insert/points/<group_id>', methods=["PUT"])
@cross_origin()
def insert_points(group_id):
    data = request.json
    api_key = data.get("key")
    app_id = data.get("appid")
    if authenticate_app(api_key, app_id):
        points = data.get("points")
        return add_points(group_id, points)
    else:
        return jsonify(m.authentication_failed)

@bp.route('/remove/points/<group_id>', methods=["PUT"])
@cross_origin()
def deduct_points(group_id):
    data = request.json
    api_key = data.get("key")
    app_id = data.get("appid")
    if authenticate_app(api_key, app_id):
        points = data.get("points")
        return remove_points(group_id, points)
    else:
        return jsonify(m.authentication_failed)

@bp.route('/get/winners', methods=["POST"])
@cross_origin()
def get_winners():
    data = request.json
    api_key = data.get("key")
    app_id = data.get("appid")
    if authenticate_app(api_key, app_id):
        category_id = data.get("category")
        return jsonify(get_groups_organized(category_id))
    else:
        return jsonify(m.authentication_failed)

@bp.route('/insert/field', methods=["POST"])
@cross_origin()
def insert_fields():
    data = request.json
    api_key = data.get("key")
    app_id = data.get("appid")
    if authenticate_app(api_key, app_id):
        new_field = {
            "fieldName": data.get("fieldName"),
            "maximum": data.get("maximum"),
            "category": data.get("category")
        }
        return insert_field(new_field)
    else:
        return jsonify(m.authentication_failed)

@bp.route('/update/field/<field_id>', methods=["PUT"])
@cross_origin()
def update_fields(field_id):
    data = request.json
    api_key = data.get("key")
    app_id = data.get("appid")
    if authenticate_app(api_key, app_id):
        updated_field = {
            "fieldName": data.get("fieldName"),
            "maximum": data.get("maximum"),
            "category": data.get("category")
        }
        return update_field(field_id ,updated_field)
    else:
        return jsonify(m.authentication_failed)

@bp.route('/remove/field/<field_id>', methods=["PUT"])
@cross_origin()
def remove_fields(field_id):
    data = request.json
    api_key = data.get("key")
    app_id = data.get("appid")
    if authenticate_app(api_key, app_id):
        return delete_field(field_id)
    else:
        return jsonify(m.authentication_failed)

@bp.route('/get/field', methods=["POST"])
@cross_origin()
def get_fields():
    data = request.json
    api_key = data.get("key")
    app_id = data.get("appid")
    if authenticate_app(api_key, app_id):
        return get_field(data.get("filter"))
    else:
        return jsonify(m.authentication_failed)


@bp.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Not found'})
