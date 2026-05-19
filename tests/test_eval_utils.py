from supportllm.eval_utils import evaluate_response

def test_evaluate_response():
    scores = evaluate_response("I am sorry about that. Please send your invoice and I will help.")
    assert scores["helpful_tone"]
    assert scores["word_count"] > 5
