package service

import (
	"app/src/utils"
	"errors"
	"runtime"

	"github.com/sirupsen/logrus"
	"gorm.io/gorm"
)

type HealthCheckService interface {
	GormCheck() error
	MemoryHeapCheck() error
}

type healthCheckService struct {
	Log *logrus.Logger
	DB  *gorm.DB
}

func NewHealthCheckService(db *gorm.DB) HealthCheckService {
	return &healthCheckService{
		Log: utils.Log,
		DB:  db,
	}
}

func (s *healthCheckService) GormCheck() error {
	sqlDB, errDB := s.DB.DB()
	if errDB != nil {
		s.Log.Errorf("failed to access the database connection pool: %v", errDB)
		return errDB
	}

	if err := sqlDB.Ping(); err != nil {
		s.Log.Errorf("failed to ping the database: %v", err)
		return err
	}

	return nil
}

func (s *healthCheckService) MemoryHeapCheck() error {
	var memStats runtime.MemStats
	runtime.ReadMemStats(&memStats)
	heapAlloc := memStats.HeapAlloc
	heapThreshold := uint64(300 * 1024 * 1024)
	s.Log.Infof("Heap Memory Allocation: %v bytes", heapAlloc)

	if heapAlloc > heapThreshold {
		s.Log.Errorf("Heap memory usage exceeds threshold: %v bytes", heapAlloc)
		return errors.New("heap memory usage too high")
	}

	return nil
}
