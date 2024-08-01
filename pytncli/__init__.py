
__app_name__ = "pytncli"
__version__ = "0.1.0"

(
    SUCCESS,
    SEND_ERROR,
    RECEIVE_ERROR,
    JSON_ERROR,
    ID_ERROR,
) = range(5)

ERRORS = {
    SEND_ERROR: "send error",
    RECEIVE_ERROR: "receive error",
    JSON_ERROR: "json error",
    ID_ERROR: "id error",
}


