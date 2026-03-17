---
mode: 'agent'
model: GPT-5.3-Codex
description: 'Update OctoFit Tracker Django app files for MongoDB and API resources'
---

# Django 앱 업데이트

- 모든 Django 프로젝트 파일은 octofit-tracker/backend/octofit_tracker 디렉터리에 있습니다.
- MongoDB 연결과 CORS 설정을 위해 settings.py를 업데이트하세요.
- users, teams, activities, leaderboard, workouts 컬렉션을 지원하도록 models.py, serializers.py, urls.py, views.py, tests.py, admin.py를 업데이트하세요.
- 루트 경로 / 가 API를 가리키고 urls.py에 api_root를 포함하세요.
- 테스트 데이터 적재를 위해 management/commands/populate_db.py를 유지하고 Django ORM으로 데이터를 처리하세요.
