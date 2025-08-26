from flask import Blueprint, request, jsonify
from .videos_models import listar_videos, criar_videos, listar_video_id, VideoNaoEncontrado


videos_blueprint = Blueprint('videos', __name__)

@videos_blueprint.route('/videos', methods=["GET"])
def get_videos():
    return jsonify(listar_videos())

@videos_blueprint.route('/videos', methods=['POST'])
def adicionar_video():
    novo_video = request.json

    new_video = criar_videos(novo_video)
    return jsonify(new_video), 201


@videos_blueprint.route('/videos/<int:id>', methods=['GET'])
def get_video_id(id):
    try:
        video = listar_video_id(id)
        return jsonify(video), 200
    except VideoNaoEncontrado:
        return jsonify({'mensagem': 'Video nao encontrado'}), 404

