from flask import Flask, request, jsonify
from recommended_course import recommended_courses

app = Flask(__name__)

def get_top_rated_course_ids():
    return jsonify({1: 1, 2: 23, 3: 23, 4: 56})

def get_recommended_courses(past_courses_id):
    return jsonify({1: 1, 2: 23, 3: 23, 4: 56})

@app.route('/', methods=['POST'])
def get_courses_id():
    data = request.get_json()

    # The courses that the user took; it's okay if it's empty
    courses_id = data.get('courses_id')

    if not courses_id:  # Check if courses_id is None or empty
        return get_top_rated_course_ids()

    return get_recommended_courses(courses_id)

if __name__ == '__main__':
    app.run(debug=True)
