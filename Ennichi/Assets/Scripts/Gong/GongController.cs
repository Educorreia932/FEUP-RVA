using UnityEngine;

public class GongController : MonoBehaviour {
	private AudioSource source;

	// Start is called before the first frame update
	void Start() {
		source = GetComponent<AudioSource>();
		source.playOnAwake = false;
	}

	void OnCollisionEnter() {
		// Plays sound whenever collision detected
		source.Play();
	}
}