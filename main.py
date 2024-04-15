import rosbag

filename = "name.bag"
bag = rosbag.Bag(filename)
for topic, msg, t in bag.read_messages(topics=['steering_angle']):
    print(msg)

bag.close()