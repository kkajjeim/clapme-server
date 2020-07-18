from flask_restful import Resource

from .auth import ApiLogin, ApiSignup
from .viewws import ApiRoutine, ApiRoutines

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


def initialize_routes(api):
    api.add_resource(HelloWorld, '/')
    api.add_resource(ApiLogin, '/login')
    api.add_resource(ApiSignup, '/signup')
    api.add_resource(ApiRoutine, '/routine', '/routine/<int:routine_id>')
    api.add_resource(ApiRoutines, '/routines')
    # api.add_resource(ApiRoutineSuccess, '/routine-success')
    # api.add_resource(ApiRoutineMaterials, '/routine-materials')
    # api.add_resource(ApiIdea, '/idea')
