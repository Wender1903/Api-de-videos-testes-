from flask import Blueprint, request, jsonify


videos_blueprint = Blueprint('videos', __name__)

@videos_blueprint.route('/videos', methods=["GET"])
def listar_videos():
    return(jsonify("Rota conectada com sucesso rota")), 200

