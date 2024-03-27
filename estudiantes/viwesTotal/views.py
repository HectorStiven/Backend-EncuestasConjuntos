from rest_framework import generics
from django.shortcuts import render
from estudiantes.models import T002DatosCasa ,T007TiposDeCasa,T003DatosConjunto,T004Personas,T005TipoAsistencia,T006TipoEncuesta,T001Encuesta
from estudiantes.serializers.estudiantes_serializers import T002DatosCasaSerializer ,T007TiposDeCasaSerializer,T003DatosConjuntoSerializer,T004PersonasSerializer,T005TipoAsistenciaSerializer,T006TipoEncuestaSerializer,T001EncuestaSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError,NotFound,PermissionDenied



class CrearT002DatosCasaVista(generics.CreateAPIView):
    queryset = T002DatosCasa.objects.all()
    serializer_class = T002DatosCasaSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'success': True, 'detail': 'Registro creado correctamente', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            raise ValidationError(e.detail)

class ListarT002DatosCasaVista(generics.ListAPIView):
    queryset = T002DatosCasa.objects.all()
    serializer_class = T002DatosCasaSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({'success': True, 'detail': 'Lista de registros', 'data': serializer.data}, status=status.HTTP_200_OK)

class BorrarT002DatosCasaVista(generics.DestroyAPIView):
    queryset = T002DatosCasa.objects.all()
    serializer_class = T002DatosCasaSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'success': True, 'detail': 'Registro eliminado correctamente'}, status=status.HTTP_204_NO_CONTENT)

class ActualizarT002DatosCasaVista(generics.UpdateAPIView):
    queryset = T002DatosCasa.objects.all()
    serializer_class = T002DatosCasaSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()  # Obtiene la instancia existente
        serializer = self.get_serializer(instance, data=request.data, partial=kwargs.get('partial', False))
        serializer.is_valid(raise_exception=True)  # Valida los datos
        serializer.save()  # Guarda la instancia con los datos actualizados
        return Response({'success': True, 'detail': 'Registro actualizado correctamente', 'data': serializer.data}, status=status.HTTP_200_OK)
    

#______________________________________________________________________________________________________________
    

class CrearT007TiposDeCasaVista(generics.CreateAPIView):
    queryset = T007TiposDeCasa.objects.all()
    serializer_class = T007TiposDeCasaSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'success': True, 'detail': 'Registro creado correctamente', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            raise ValidationError(e.detail)

class ListarT007TiposDeCasaVista(generics.ListAPIView):
    queryset = T007TiposDeCasa.objects.all()
    serializer_class = T007TiposDeCasaSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({'success': True, 'detail': 'Lista de registros', 'data': serializer.data}, status=status.HTTP_200_OK)

class BorrarT007TiposDeCasaVista(generics.DestroyAPIView):
    queryset = T007TiposDeCasa.objects.all()
    serializer_class = T007TiposDeCasaSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'success': True, 'detail': 'Registro eliminado correctamente'}, status=status.HTTP_204_NO_CONTENT)

class ActualizarT007TiposDeCasaVista(generics.UpdateAPIView):
    queryset = T007TiposDeCasa.objects.all()
    serializer_class = T007TiposDeCasaSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()  # Obtiene la instancia existente
        serializer = self.get_serializer(instance, data=request.data, partial=kwargs.get('partial', False))
        serializer.is_valid(raise_exception=True)  # Valida los datos
        serializer.save()  # Guarda la instancia con los datos actualizados
        return Response({'success': True, 'detail': 'Registro actualizado correctamente', 'data': serializer.data}, status=status.HTTP_200_OK)





class CrearT003DatosConjuntoVista(generics.CreateAPIView):
    queryset = T003DatosConjunto.objects.all()
    serializer_class = T003DatosConjuntoSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'success': True, 'detail': 'Registro creado correctamente', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            raise ValidationError(e.detail)

class ListarT003DatosConjuntoVista(generics.ListAPIView):
    queryset = T003DatosConjunto.objects.all()
    serializer_class = T003DatosConjuntoSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({'success': True, 'detail': 'Lista de registros', 'data': serializer.data}, status=status.HTTP_200_OK)

class BorrarT003DatosConjuntoVista(generics.DestroyAPIView):
    queryset = T003DatosConjunto.objects.all()
    serializer_class = T003DatosConjuntoSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'success': True, 'detail': 'Registro eliminado correctamente'}, status=status.HTTP_204_NO_CONTENT)

class ActualizarT003DatosConjuntoVista(generics.UpdateAPIView):
    queryset = T003DatosConjunto.objects.all()
    serializer_class = T003DatosConjuntoSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()  # Obtiene la instancia existente
        serializer = self.get_serializer(instance, data=request.data, partial=kwargs.get('partial', False))
        serializer.is_valid(raise_exception=True)  # Valida los datos
        serializer.save



class CrearT004PersonasVista(generics.CreateAPIView):
    queryset = T004Personas.objects.all()
    serializer_class = T004PersonasSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'success': True, 'detail': 'Registro creado correctamente', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            raise ValidationError(e.detail)

class ListarT004PersonasVista(generics.ListAPIView):
    queryset = T004Personas.objects.all()
    serializer_class = T004PersonasSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({'success': True, 'detail': 'Lista de registros', 'data': serializer.data}, status=status.HTTP_200_OK)

class BorrarT004PersonasVista(generics.DestroyAPIView):
    queryset = T004Personas.objects.all()
    serializer_class = T004PersonasSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'success': True, 'detail': 'Registro eliminado correctamente'}, status=status.HTTP_204_NO_CONTENT)

class ActualizarT004PersonasVista(generics.UpdateAPIView):
    queryset = T004Personas.objects.all()
    serializer_class = T004PersonasSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=kwargs.get('partial', False))
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True, 'detail': 'Registro actualizado correctamente', 'data': serializer.data}, status=status.HTTP_200_OK)
    



class CrearT005TipoAsistenciaVista(generics.CreateAPIView):
    queryset = T005TipoAsistencia.objects.all()
    serializer_class = T005TipoAsistenciaSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'success': True, 'detail': 'Registro creado correctamente', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            raise ValidationError(e.detail)

class ListarT005TipoAsistenciaVista(generics.ListAPIView):
    queryset = T005TipoAsistencia.objects.all()
    serializer_class = T005TipoAsistenciaSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({'success': True, 'detail': 'Lista de registros', 'data': serializer.data}, status=status.HTTP_200_OK)

class BorrarT005TipoAsistenciaVista(generics.DestroyAPIView):
    queryset = T005TipoAsistencia.objects.all()
    serializer_class = T005TipoAsistenciaSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'success': True, 'detail': 'Registro eliminado correctamente'}, status=status.HTTP_204_NO_CONTENT)

class ActualizarT005TipoAsistenciaVista(generics.UpdateAPIView):
    queryset = T005TipoAsistencia.objects.all()
    serializer_class = T005TipoAsistenciaSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=kwargs.get('partial', False))
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True, 'detail': 'Registro actualizado correctamente', 'data': serializer.data}, status=status.HTTP_200_OK)
    

class CrearT006TipoEncuestaVista(generics.CreateAPIView):
    queryset = T006TipoEncuesta.objects.all()
    serializer_class = T006TipoEncuestaSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'success': True, 'detail': 'Registro creado correctamente', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            raise ValidationError(e.detail)


class ListarT006TipoEncuestaVista(generics.ListAPIView):
    queryset = T006TipoEncuesta.objects.all()
    serializer_class = T006TipoEncuestaSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({'success': True, 'detail': 'Lista de registros', 'data': serializer.data}, status=status.HTTP_200_OK)


class BorrarT006TipoEncuestaVista(generics.DestroyAPIView):
    queryset = T006TipoEncuesta.objects.all()
    serializer_class = T006TipoEncuestaSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'success': True, 'detail': 'Registro eliminado correctamente'}, status=status.HTTP_204_NO_CONTENT)


class ActualizarT006TipoEncuestaVista(generics.UpdateAPIView):
    queryset = T006TipoEncuesta.objects.all()
    serializer_class = T006TipoEncuestaSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()  # Obtiene la instancia existente
        serializer = self.get_serializer(instance, data=request.data, partial=kwargs.get('partial', False))
        serializer.is_valid(raise_exception=True)  # Valida los datos
        serializer.save()  # Guarda la instancia con los datos actualizados
        return Response({'success': True, 'detail': 'Registro actualizado correctamente', 'data': serializer.data}, status=status.HTTP_200_OK)
    



class CrearT001EncuestaVista(generics.CreateAPIView):
    queryset = T001Encuesta.objects.all()
    serializer_class = T001EncuestaSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'success': True, 'detail': 'Registro creado correctamente', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            raise ValidationError(e.detail)


class ListarT001EncuestaVista(generics.ListAPIView):
    queryset = T001Encuesta.objects.all()
    serializer_class = T001EncuestaSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({'success': True, 'detail': 'Lista de registros', 'data': serializer.data}, status=status.HTTP_200_OK)


class BorrarT001EncuestaVista(generics.DestroyAPIView):
    queryset = T001Encuesta.objects.all()
    serializer_class = T001EncuestaSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'success': True, 'detail': 'Registro eliminado correctamente'}, status=status.HTTP_204_NO_CONTENT)


class ActualizarT001EncuestaVista(generics.UpdateAPIView):
    queryset = T001Encuesta.objects.all()
    serializer_class = T001EncuestaSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()  # Obtiene la instancia existente
        serializer = self.get_serializer(instance, data=request.data, partial=kwargs.get('partial', False))
        serializer.is_valid(raise_exception=True)  # Valida los datos
        serializer.save()  # Guarda la instancia con los datos actualizados
        return Response({'success': True, 'detail': 'Registro actualizado correctamente', 'data': serializer.data}, status=status.HTTP_200_OK)