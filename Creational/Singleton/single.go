package main

import (
	"fmt"
	"sync"
)

type Singleton struct {
	data string
}

var instance *Singleton
var once sync.Once
var mutex = &sync.Mutex{}

func GetInstance() *Singleton {
	mutex.Lock()
	defer mutex.Unlock()
	if instance == nil {
		fmt.Println("Creating First Instance")
		once.Do(func() {
			instance = &Singleton{data: "initial data"}
		})
	} else {
		fmt.Println("Instance already created")
	}
	return instance
}
func (s *Singleton) GetData() string {
	return s.data
}
func (s *Singleton) SetData(data string) {
	s.data = data
}
func (s *Singleton) DoSomething() {
	fmt.Println("Just Doin random stuff")
}

func main() {
	// s1 := GetInstance()
	// s2 := GetInstance()
	// s1.SetData("New Data of S1")
	// fmt.Println(s1.GetData())
	// fmt.Println(s2.GetData())

	for i := 0; i < 5; i++ {
		go GetInstance()
	}
	fmt.Scanln()

}
