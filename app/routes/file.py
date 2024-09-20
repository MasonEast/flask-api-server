import jwt
from datetime import timedelta
import os

from flask_restx import Namespace, Resource, fields
from flask import request, send_from_directory



file_ns = Namespace('file', description='文件处理')

@file_ns.route('/download/<string:filename>')
class FileDownload(Resource):
    def get(self, filename):
        try:
            # 文件路径
            directory = os.path.join(os.getcwd(), 'files')
            return send_from_directory(directory, filename, as_attachment=True)
        except Exception as e:
            file_ns.abort(404, str(e))