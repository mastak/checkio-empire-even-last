from checkio_referee import RefereeBase


import settings_env
from tests import TESTS


class Referee(RefereeBase):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS
    DEFAULT_FUNCTION_NAME = "even_last"
    FUNCTION_NAMES = {
        "javascript": "evenLast"
    }

    @gen.coroutine
    def post_test(self, test, validator_result, category_name, test_number):
        yield super().post_test(test, validator_result, category_name, test_number)
        yield self.editor_client.send_post_test({
            'test_id': test_number, 
            'message': "Test passed"
        })
