from rest_framework import serializers
import requests
from .models import PackageRelease, Project


def consult_package_pypi(name_pakage):
    url = f'https://pypi.org/pypi/{name_pakage}/json'

    res = requests.get(url=url)

    if res.status_code >= 200 and res.status_code <= 299:
        return {
            "status": res.status_code,
            "name": name_pakage,
            "version": res.json()['info']['version']}
    return {"status": res.status_code}


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageRelease
        fields = ['name', 'version']
        extra_kwargs = {'version': {'required': False}}


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'packages']

    packages = PackageSerializer(many=True)

    def generate_new_package(self, packages):
        new_packages = []
        for package in packages:
            result = consult_package_pypi(package['name'])
            if result['status'] != 200:
                raise serializers.ValidationError({
                    "error": "One or more packages doesn't exist"
                })
                return
            if 'version' not in package:
                package = {'name': package['name'],
                           'version': result['version']}

            new_packages.append(package)
        return new_packages

    def create(self, validated_data):
        new_packages = self.generate_new_package(validated_data["packages"])

        validated_data["packages"] = new_packages
        packages = validated_data["packages"]

        project = Project.objects.create(name=validated_data['name'])
        for package in packages:
            PackageRelease.objects.create(
                project=project, name=package['name'], version=package['version'])

        return Project(name=validated_data['name'])
