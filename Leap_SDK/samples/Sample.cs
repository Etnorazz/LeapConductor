/******************************************************************************\
* Copyright (C) 2012 Leap Motion, Inc. All rights reserved.                    *
* NOTICE: This developer release of Leap Motion, Inc. software is confidential *
* and intended for very limited distribution. Parties using this software must *
* accept the SDK Agreement prior to obtaining this software and related tools. *
* This software is subject to copyright.                                       *
\******************************************************************************/

using System;
using System.Threading;

class SampleListener : Listener {
  private Object thisLock = new Object();

  private void SafeWriteLine(String line) {
    lock(thisLock) {
      Console.WriteLine(line);
    }
  }

  public override void onInit(Controller controller) {
    SafeWriteLine("Initialized");
  }

  public override void onConnect(Controller controller) {
    SafeWriteLine("Connected");
  }

  public override void onDisconnect(Controller controller) {
    SafeWriteLine("Disconnected");
  }

  public override void onFrame(Controller controller) {
    // Get the most recent frame and report some basic information
    Frame frame = controller.frame();
    HandArray hands = frame.hands();
    int numHands = hands.Count;
    SafeWriteLine("Frame id: " + frame.id()
                + ", timestamp: " + frame.timestamp()
                + ", hands: " + numHands);

    if (numHands >= 1) {
      // Get the first hand
      Hand hand = hands[0];

      // Check if the hand has any fingers
      FingerArray fingers = hand.fingers();
      int numFingers = fingers.Count;
      if (numFingers >= 1) {
        // Calculate the hand's average finger tip position
        Vector pos = new Vector(0, 0, 0);
        foreach (Finger finger in fingers) {
          Ray tip = finger.tip();
          pos.x += tip.position.x;
          pos.y += tip.position.y;
          pos.z += tip.position.z;
        }
        pos = new Vector(pos.x/numFingers, pos.y/numFingers, pos.z/numFingers);
        SafeWriteLine("Hand has " + numFingers + " fingers with average tip position"
                    + " (" + pos.x.ToString("n2") + ", " + pos.y.ToString("n2")
                    + ", " + pos.z.ToString("n2") + ")");
      }

      // Check if the hand has a palm
      Ray palmRay = hand.palm();
      if (palmRay != null) {
        // Get the palm position and wrist direction
        Vector palm = palmRay.position;
        Vector wrist = palmRay.direction;
        SafeWriteLine("Palm position: (" + palm.x.ToString("n2") + ", "
                                         + palm.y.ToString("n2") + ", "
                                         + palm.z.ToString("n2") + ")");

        // Check if the hand has a normal vector
        Vector normal = hand.normal();
        if (normal != null) {
          // Calculate the hand's pitch, roll, and yaw angles
          double pitchAngle = Math.Atan2(normal.z, normal.y) * 180/Math.PI + 180;
          double rollAngle = Math.Atan2(normal.x, normal.y) * 180/Math.PI + 180;
          double yawAngle = Math.Atan2(wrist.z, wrist.x) * 180/Math.PI - 90;
          // Ensure the angles are between -180 and +180 degrees
          if (pitchAngle > 180) pitchAngle -= 360;
          if (rollAngle > 180) rollAngle -= 360;
          if (yawAngle > 180) yawAngle -= 360;
          SafeWriteLine("Pitch: " + pitchAngle.ToString("n0") + " degrees,  "
                      + "roll: " + rollAngle.ToString("n0") + " degrees,  "
                      + "yaw: " + yawAngle.ToString("n0") + " degrees");
        }
      }

      // Check if the hand has a ball
      Ball ball = hand.ball();
      if (ball != null) {
        SafeWriteLine("Hand curvature radius: " + ball.radius.ToString("n2") + " mm");
      }
    }
  }
}

class Sample {
  public static void Main() {
    // Create a sample listener and assign it to a controller to receive events
    SampleListener listener = new SampleListener();
    Controller controller = new Controller(listener);

    // Keep this process running until Enter is pressed
    Console.WriteLine("Press Enter to quit...");
    Console.ReadLine();

    // The controller must be disposed of before the listener
    controller.Dispose();
  }
}
