from config import db

class Video(db.Model):
    __tablename__ = 'videos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(274), nullable=False)
    categoria = db.Column(db.String(23), nullable=False)
    descricao = db.Column(db.String(320), nullable=False)
    video = db.Column(db.String(1500), nullable=False)

    def __init__(self, nome, categoria, descricao, video):
        self.nome = nome
        self.categoria = categoria
        self.descricao = descricao
        self.video = video

    def exibir_informacoes(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'categoria': self.categoria,
            'descricao': self.descricao,
            'video': self.video
        }

class VideoNaoEncontrado(Exception):
    pass

def listar_videos():
    videos = Video.query.all()
    return [video.exibir_informacoes() for video in videos]

def listar_video_id(id):
    video = Video.query.get(id)
    if not video:
        raise VideoNaoEncontrado
    return video.exibir_informacoes()
    

def criar_videos(novo_video):
    new_video = Video(
        nome=str(novo_video['nome']),
        categoria=str(novo_video['categoria']),
        descricao=str(novo_video['descricao']),
        video=str(novo_video['video'])
    )

    db.session.add(new_video)
    db.session.commit()
    return new_video.exibir_informacoes()

def deletar_video(id):
    video = Video.query.get(id)

    if not video:
        raise VideoNaoEncontrado
    db.session.delete(video)
    db.session.commit()