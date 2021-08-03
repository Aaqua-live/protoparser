import protoparser

SCHEMA_WITH_ONEOF = """
syntax = "proto3";

message TestMessage {
    string uuid = 1;

    oneof PAYLOAD {
        string field1 = 1;
        string field2 = 2;
    }
}
"""

SCHEMA_WITH_TWO_MESSAGES = """
syntax = "proto3";

message TestMessage1 {
    string uuid = 1;
}

message TestMessage2 {
    string uuid = 1;
}
"""

SCHEMA_WITH_NESTED_MESSAGES = """
syntax = "proto3";

message TestMessage1 {
    string uuid = 1;
    TestMessage2 msg = 2;

    message TestMessage2 {
        string uuid = 1;
    }
}
"""

SCHEMA_WITH_ENUM = """
syntax = "proto3";

message TestMessage1 {
    string uuid = 1;
    testEnum state = 2;

    enum testEnum {
        idle = 0;
        spinning = 1;
        broken = 2;
    }
}
"""

SCHEMA_COMPLEX = """
syntax = "proto3";

message TestMessage1 {
    string uuid = 1;
    TestMessage2 msg2 = 2;

    message TestMessage3 {
        int aNumber = 1;
        string aString = 2;
    }

    TestMessage3 msg3 = 3;

    oneof payload {
        // This is a comment
        TestMessage3 msg4 = 1;
        // This is another comment
        string something = 2;
    }
}

message TestMessage2 {
    int value = 1;
    aEnum myEnum = 2;

    enum aEnum {
        idle = 0;
        spinning = 1;
        broken = 2;
    }
}
"""

def test_protobuf_oneof():
    proto = protoparser.parse(SCHEMA_WITH_ONEOF)
    assert 1 == len(proto.messages)                                            # must have one message only
    assert 1 == len(proto.messages['TestMessage'].fields)                      # must have one primitive field only
    assert 1 == len(proto.messages['TestMessage'].oneofs)                      # must have one oneof only
    assert 2 == len(proto.messages['TestMessage'].oneofs['PAYLOAD'].fields)    # must have two fields in the oneof

def test_protobuf_two_msgs():
    proto = protoparser.parse(SCHEMA_WITH_TWO_MESSAGES)
    assert 2 == len(proto.messages)

def test_nested_messages():
    proto = protoparser.parse(SCHEMA_WITH_NESTED_MESSAGES)
    assert 1 == len(proto.messages)
    assert 2 == len(proto.messages['TestMessage1'].fields)
    assert 1 == len(proto.messages['TestMessage1'].messages)
    assert 1 == len(proto.messages['TestMessage1'].messages['TestMessage2'].fields)

def test_enum():
    proto = protoparser.parse(SCHEMA_WITH_ENUM)
    assert 1 == len(proto.messages)
    assert 2 == len(proto.messages['TestMessage1'].fields)
    assert 1 == len(proto.messages['TestMessage1'].enums)
    assert 3 == len(proto.messages['TestMessage1'].enums['testEnum'])

def test_complex():
    proto = protoparser.parse(SCHEMA_COMPLEX)
    assert 2 == len(proto.messages)
    assert 3 == len(proto.messages['TestMessage1'].fields)
    assert 1 == len(proto.messages['TestMessage1'].messages)
    assert 2 == len(proto.messages['TestMessage1'].messages['TestMessage3'].fields)
    assert 2 == len(proto.messages['TestMessage2'].fields)
    assert 1 == len(proto.messages['TestMessage2'].enums)
    assert 3 == len(proto.messages['TestMessage2'].enums['aEnum'])
    assert 1 == len(proto.messages['TestMessage1'].oneofs)
    assert 2 == len(proto.messages['TestMessage1'].oneofs['payload'].fields)
    assert '// This is a comment\n' == proto.messages['TestMessage1'].oneofs['payload'].fields[0].comment.content
    assert '// This is another comment\n' == proto.messages['TestMessage1'].oneofs['payload'].fields[1].comment.content

if __name__ == '__main__':
    test_protobuf_oneof()