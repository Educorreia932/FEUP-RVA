using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GongController : MonoBehaviour
{
    private AudioSource source;

    // Start is called before the first frame update
    void Start()
    {
        source = GetComponent<AudioSource>();
        source.playOnAwake = false;
        if (source.clip == null)
        {
            Debug.LogWarning("Gong " + gameObject.name + " has no clip attached in its audio source.");
        }
    }

    void OnCollisionEnter()  //Plays Sound Whenever collision detected
    {
        source.Play();
    }
}
