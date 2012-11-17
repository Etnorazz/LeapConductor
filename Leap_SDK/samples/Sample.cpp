/******************************************************************************\
* Copyright (C) 2012 Leap Motion, Inc. All rights reserved.                    *
* NOTICE: This developer release of Leap Motion, Inc. software is confidential *
* and intended for very limited distribution. Parties using this software must *
* accept the SDK Agreement prior to obtaining this software and related tools. *
* This software is subject to copyright.                                       *
\******************************************************************************/

#define _HAS_ITERATOR_DEBUGGING 0 // Visual Studio STL iterator debug workaround
#include "Leap.h"

#include <iostream>

#define _USE_MATH_DEFINES // To get definition of M_PI
#include <math.h>

class SampleListener : public Leap::Listener {
  public:
    virtual void onInit(const Leap::Controller&);
    virtual void onConnect(const Leap::Controller&);
    virtual void onDisconnect(const Leap::Controller&);
    virtual void onFrame(const Leap::Controller&);
};

void SampleListener::onInit(const Leap::Controller& controller) {
  std::cout << "Initialized" << std::endl;
}

void SampleListener::onConnect(const Leap::Controller& controller) {
  std::cout << "Connected" << std::endl;
}

void SampleListener::onDisconnect(const Leap::Controller& controller) {
  std::cout << "Disconnected" << std::endl;
}

void SampleListener::onFrame(const Leap::Controller& controller) {
  // Get the most recent frame and report some basic information
  const Leap::Frame frame = controller.frame();
  const std::vector<Leap::Hand>& hands = frame.hands();
  const size_t numHands = hands.size();
  std::cout << "Frame id: " << frame.id()
            << ", timestamp: " << frame.timestamp()
            << ", hands: " << numHands << std::endl;

  if (numHands >= 1) {
    // Get the first hand
    const Leap::Hand& hand = hands[0];

    // Check if the hand has any fingers
    const std::vector<Leap::Finger>& fingers = hand.fingers();
    const size_t numFingers = fingers.size();
    if (numFingers >= 1) {
      // Calculate the hand's average finger tip position
      Leap::Vector pos(0, 0, 0);
      for (size_t i = 0; i < numFingers; ++i) {
        const Leap::Finger& finger = fingers[i];
        const Leap::Ray& tip = finger.tip();
        pos.x += tip.position.x;
        pos.y += tip.position.y;
        pos.z += tip.position.z;
      }
      pos = Leap::Vector(pos.x/numFingers, pos.y/numFingers, pos.z/numFingers);
      std::cout << "Hand has " << numFingers << " fingers with average tip position"
                << " (" << pos.x << ", " << pos.y << ", " << pos.z << ")" << std::endl;
    }

    // Check if the hand has a palm
    const Leap::Ray* palmRay = hand.palm();
    if (palmRay != NULL) {
      // Get the palm position and wrist direction
      const Leap::Vector palm = palmRay->position;
      const Leap::Vector wrist = palmRay->direction;
      std::cout << "Palm position: ("
                << palm.x << ", " << palm.y << ", " << palm.z << ")" << std::endl;

      // Check if the hand has a normal vector
      const Leap::Vector* normal = hand.normal();
      if (normal != NULL) {
        // Calculate the hand's pitch, roll, and yaw angles
        double pitchAngle = atan2(normal->z, normal->y) * 180/M_PI + 180;
        double rollAngle = atan2(normal->x, normal->y) * 180/M_PI + 180;
        double yawAngle = atan2(wrist.z, wrist.x) * 180/M_PI - 90;
        // Ensure the angles are between -180 and +180 degrees
        if (pitchAngle > 180) pitchAngle -= 360;
        if (rollAngle > 180) rollAngle -= 360;
        if (yawAngle > 180) yawAngle -= 360;
        std::cout << "Pitch: " << pitchAngle << " degrees,  "
                  << "roll: " << rollAngle << " degrees,  "
                  << "yaw: " << yawAngle << " degrees" << std::endl;
      }
    }

    // Check if the hand has a ball
    const Leap::Ball* ball = hand.ball();
    if (ball != NULL) {
      std::cout << "Hand curvature radius: " << ball->radius << " mm" << std::endl;
    }
  }
}

int main() {
  // Create a sample listener and assign it to a controller to receive events
  SampleListener listener;
  Leap::Controller controller(&listener);

  // Keep this process running until Enter is pressed
  std::cout << "Press Enter to quit..." << std::endl;
  std::cin.get();
}
