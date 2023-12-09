using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DartsGameManager : MonoBehaviour
{
    public Transform spawnPoint;
    public GameObject dartPrefab;
    // Start is called before the first frame update
    void Start()
    {
        GameObject dart = Instantiate(dartPrefab, spawnPoint);
        dart.GetComponent<Rigidbody>().velocity = new Vector3(0.0f, 0.0f, 10.0f);
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
