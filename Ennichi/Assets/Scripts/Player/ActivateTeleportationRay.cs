using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.XR.Interaction.Toolkit;

public class ActivateTeleportationRay : MonoBehaviour {
	public GameObject leftTeleportation;
	public GameObject rightTeleportation;
	
	public XRRayInteractor leftRay;
	public XRRayInteractor rightRay;

	void Update() {
		bool isLeftRayHovering =
			leftRay.TryGetHitInfo(
				out Vector3 leftPos,
				out Vector3 leftNormal,
				out int leftNumber,
				out bool leftValid
			);
		
		bool isRightRayHovering =
			leftRay.TryGetHitInfo(
				out Vector3 rightPos,
				out Vector3 rightNormal,
				out int rightNumber,
				out bool rightValid
			);
		
		leftTeleportation.SetActive(!isLeftRayHovering);
		rightTeleportation.SetActive(!isRightRayHovering);
	}
}