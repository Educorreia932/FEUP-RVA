using UnityEngine;
using UnityEngine.InputSystem;

public class AnimateHandOnInput : MonoBehaviour {
	public InputActionProperty pinchAnimationAction;
	public InputActionProperty gripAnimationAction;
	public Animator handAnimator; 
	
	void Start() {
	}

	void Update() {
		float triggerValue = pinchAnimationAction.action.ReadValue<float>();
		float gripValue = gripAnimationAction.action.ReadValue<float>();
		
		handAnimator.SetFloat("Trigger", triggerValue);
		handAnimator.SetFloat("Grip", gripValue);
	}
}