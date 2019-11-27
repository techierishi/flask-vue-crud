import cv2
import os
import tensorflow as tf
import preprocessor


def main(author):
    print('OpenCV version {} '.format(cv2.__version__))

    current_dir = os.path.dirname(__file__)

    training_folder = os.path.join(current_dir, 'data/training/', author)
    test_folder = os.path.join(current_dir, 'data/test/', author)

    training_data = []
    training_labels = []
    for filename in os.listdir(training_folder):
        img = cv2.imread(os.path.join(training_folder, filename), 0)
        if img is not None:
            data = preprocessor.prepare(img)
            training_data.append(data)
            training_labels.append([0, 1] if "genuine" in filename else [1, 0])

    test_data = []
    test_labels = []
    for filename in os.listdir(test_folder):
        img = cv2.imread(os.path.join(test_folder, filename), 0)
        if img is not None:
            data = preprocessor.prepare(img)
            test_data.append(data)
            test_labels.append([0, 1] if "genuine" in filename else [1, 0])

    return sgd(training_data, training_labels, test_data, test_labels)


# Softmax Regression Model
def regression(x):
    W = tf.Variable(tf.zeros([901, 2]), name="W")
    b = tf.Variable(tf.zeros([2]), name="b")
    y = tf.nn.softmax(tf.matmul(x, W) + b)
    return y, [W, b]


def sgd(training_data, training_labels, test_data, test_labels):
    tf.compat.v1.disable_eager_execution()
    # model
    with tf.compat.v1.variable_scope("regression"):
        x = tf.compat.v1.placeholder(tf.float32, [None, 901])
        y, variables = regression(x)

    # train
    y_ = tf.compat.v1.placeholder("float", [None, 2])
    cross_entropy = -tf.reduce_sum(y_ * tf.compat.v1.log(y))
    train_step = tf.compat.v1.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
    correct_prediction = tf.compat.v1.equal(tf.compat.v1.argmax(y, 1), tf.compat.v1.argmax(y_, 1))
    accuracy = tf.compat.v1.reduce_mean(tf.compat.v1.cast(correct_prediction, tf.compat.v1.float32))

    with tf.compat.v1.Session() as sess:
        sess.run(tf.compat.v1.global_variables_initializer())
        sess.run(train_step, feed_dict={x: training_data, y_: training_labels})
        testresult = sess.run(accuracy, feed_dict={x: test_data, y_: test_labels})
        print('testresult',testresult)
        return testresult

if __name__ == '__main__':
    main('029')