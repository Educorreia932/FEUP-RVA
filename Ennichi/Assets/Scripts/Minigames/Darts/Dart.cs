using UnityEngine;

public class Dart : MonoBehaviour {
	void Update() {
		// Lock rotation
		transform.eulerAngles = new Vector3(0f, 180f, 0f);
	}
}