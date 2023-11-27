using UnityEngine;

public class PlayerController : MonoBehaviour {
	private float speed = 5;
	private CharacterController controller;

	// Start is called before the first frame update
	void Start() {
		controller = GetComponent<CharacterController>();
	}

	// Update is called once per frame
	void Update() {
		// Get input
		Vector3 input = new(
			Input.GetAxisRaw("Horizontal"),
			0,
			Input.GetAxisRaw("Vertical")
		);

		input = input.normalized;

		Vector3 velocity = input * speed;

		// Move player
		controller.Move(velocity * Time.deltaTime);
	}
}