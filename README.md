# ROS_bootcamp
Repository that talks about all basic features of ROS as a part of the ROS.
## 1.  What is ROS, and its merits and limitations for Roboticists?

##      ROS:

- ROS stays for Robot Operating System. It's not a real operating system ,it is more like an environment. The big strength of ROS is the ability of connecting nodes together. Nodes are pieces of software that can be written in C++, Python. Its basically develop in Python.

   * ROS is an open-source, meta-operating system for  robot. It provides the services  from an operating system, including hardware abstraction, low-level device control, implementation of commonly-used functionality, message-passing between processes, and package management. 

   * A software framework for programming robots.

   * Prototypes originated from Stanford AI research, officially created and developed by Willow Garage starting in 2007.

   * Currently maintained by Open Source Robotics Foundation.

   * Consists of infrastructure, tools, capabilities, and ecosystem.

   * It also provides tools and libraries for obtaining, building, writing, and running code across multiple computers. 

     **MERITS**:

* It allows flexibility for code written in ROS to be run  in other robotics software frameworks.

* Its open source to adopt the code written by other developers for own reference or work.

* It allows easier management which peer-to-peer communication for complicated multi-board robots.

* It runs on multi language like Python,C++,Octave etc.

* In industry Standard tool most commercial sensors and actuators have ROS drivers .

* Strongly integration with third party environments.

  **LIMITATIONS:**

* Powerful hardware required to run ROS on Robot.

* Not useful in developing novel applications where reusing of packages is not preferred,and thus requires lots of time-consuming modifications.

* Since ROS must support a large range of topologies and frameworks, messages sent via ROS are often duplicated taking up more bandwidth than necessary.

* Not a real-time system (inherent latency in processes).

* Security issues for industrial deployment scenarios.

  

## 2.**Explain  the basic ROS terminology:**

 i. **Workspace**

- All of the development you do for ROS must be done in your ROS workspace. This is so ROS knows where to look for all of the programs you write and their respective utilities and resources.

 ii. **ROS** **package**

- A package is a container for closely related nodes and utilities used by those nodes. Include files, message definitions, resources, etc. are stored along with nodes inside a package. As an example, imagine a robot with many different sensors, such as IR rangefinders, sonar, laser scanners, and encoders. Each of these types of sensors would ideally have their own node. Because these nodes are all for sensors, you might group them into a package called *my_robots_sensor_drivers*.

 iii. **Nodes**

- A ROS node is a simple program that publishes or subscribes to a topic or contains a program that enables a ROS service. It should be highly specialized and accomplish a single task. Nodes communicate with other nodes by sending messages, which will be discussed later. Examples of tasks which should be carried out in a specific node are:
  - Controlling motors
  - Interpreting commands from an input source
  - Planning a path to drive on
  - Reading a specific sensor.

iv. **Topics** 

- ROS topics are named buses that allow nodes to pass messages. A ROS topic can be published to, or subscribed to with many different message types. This setup allows the publishing and subscribing to happen completely independent of each other assuming they have matching message types.

v. **Messages** 

- ROS Messages are the individual sets of data that are published to a topic. Messages can have many different types but the standard messages can be found here. The fields in messages can be any of the base types or another message. Common Message types can be found here.

vi. **Services**

- A ROS service is an object that can be called similar to a function from other nodes. It allows a request and a reply. An example might be an "add two ints" service.
# Publisher and Subscriber:

ROS nodes mechanism is to exchange data by sending and receiving messages, which transmitted on a topic, and each topic has a unique name .

 If a node wants to share information, the one who send data to a topic is publisher. 

And that one who wants to receive that information is subscriber on that same topic.

## Some functions:

### 1.Rosrun:

It allows  to use the package name to run directly  a node within a package without  know its path.

### 2.Rostopic list:

It returns a list of ROS topics from the ROS master. It display a list of current topics.

### 3.Rostopic echo:

It display messages published to a topic.

### 4.Rosmsg show:

It is a command-line tool for displaying information about ROS Message types.

#       ASSIGNMENT 3



## 1,a. What is the ROS navigation stack?

- A  navigation stack that takes in information from odometry, sensor streams, and a goal pose and outputs safe velocity commands that are sent to a mobile base.
- Map provided by a Map Server. Each module is a node. Planner has a layered architecture . Obstacle sensing refined on-line by appropriate modules .

## b. What is localization? What sensors are used for localization?

- Localization is a way to determine the location of sensor nodes.

-  It determine the current robot position, the measurements up to the current instant and a map.

-  The important function of a sensor network is to collect and forward data to destination. 
-  This kind of information can be obtained using localization technique in wireless sensor networks (WSNs). 
-  Interoceptive sensors, like wheel odometers and IMUs, generate relative position measurements.
- Exteroceptive sensors, including cameras and lasers, provide absolute position measurements.
- **Acoustic Sensors** use the Time of Flight  technique to measure location.
- **Laser Rangefinders** also use TOF and phase-shift techniques to measure position.
- **Visual Sensors** are mainly three types: monocular cameras, stereo cameras, and RGB-D cameras. 

## c. What is the meaning of mapping?

* process of modelling the robot environment using sensor data.

* Given a robot that has a perfect ego- estimate of the position, and a sequence of measurements, determine the map of the environment. 

* A perfect estimate of the robot pose is usually not available. 

* Instead we solve a more complex problem: Simultaneous Localization and Mapping (SLAM).



## d. What is tf in ROS and why is it needed?

* tf is a package that lets the user keep track of multiple coordinate frames over time. 
* tf maintains the relationship between coordinate frames in a tree structure buffered in time, and lets the user transform points, vectors, etc between any two coordinate frames at any desired point in time.



## e. What is the SLAM problem?

    GIVEN
    * the robots controls 
    u1:T={u1,u2,u3......uT}
     * observations
     z1:T={z1,z2,z3.......zT}
    WANTED
    * map of the environment
     m
    * path of the robot
    x0:T={x0,x1,x2..,xT}


