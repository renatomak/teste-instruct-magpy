from rest_framework import serializers
import requests
from api.models import PackageRelease, Project


def consult_package_pypi(package):
    name = package['name']

    if "version" in package:
        version = package['version']
        url = f'https://pypi.org/pypi/{name}/{version}/json'
    else:
        url = f'https://pypi.org/pypi/{name}/json'

    res = requests.get(url=url)
    if res.status_code != 200:
        raise serializers.ValidationError({
            "error": "One or more packages doesn't exist"
        })
    if "version" not in package:
        version = res.json()['info']['version']

    return {
        "status": res.status_code,
        "name": name,
        "version": version}


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
            new_package = consult_package_pypi(package)
            new_packages.append(new_package)
        return new_packages

    def create(self, validated_data):
        new_packages = self.generate_new_package(validated_data["packages"])

        validated_data["packages"] = new_packages
        packages = validated_data["packages"]

        project = Project.objects.create(name=validated_data['name'])

        for package in packages:
            PackageRelease.objects.create(
                project=project,
                name=package['name'],
                version=package['version'])

        return project

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
