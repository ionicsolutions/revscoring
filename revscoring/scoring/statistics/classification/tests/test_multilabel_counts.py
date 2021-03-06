import json
import pickle

from ..counts import MultilabelCounts


def test_counts():
    c = MultilabelCounts(
        ["foo", "bar", "baz"],
        [({'prediction': ["foo"]}, ["foo", "bar"])] * 10 +
        [({'prediction': ["foo", "bar", "baz"]}, ["foo", "baz"])] * 20 +
        [({'prediction': ["bar"]}, ["bar"])] * 30 +
        [({'prediction': ["baz"]}, ["bar", "baz"])] * 40,
        'prediction'
    )

    print(c.format_str({}))
    print(json.dumps(c.format_json({}), indent=2))
    assert c.lookup("n") == 100
    assert c.lookup("labels.foo") == 30
    assert c.lookup("predictions.foo.true.false") == 0
    assert c.lookup("predictions.foo.true.true") == 30
    assert c.lookup("predictions.bar.false.true") == 20

    pickle.loads(pickle.dumps(c))
