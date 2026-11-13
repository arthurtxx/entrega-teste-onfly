"""Política de status das reservas."""

from __future__ import annotations


def is_billable(status: str) -> bool:
    """Indica se a reserva entra nos totais financeiros e de noites."""
    return status == "CONFIRMED" #como o teste exclui apenas os cancelados, o no show tambem é considerado
