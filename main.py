#!/usr/bin/env python3
import sys
import argparse
from utils.storage import load_database, save_database
from models.user import User
from models.project import Project
from models.task import Task

# Load rich styling assets safely
from rich.console import Console
from rich.table import Table

console = Console()

def run_cli():
    parser = argparse.ArgumentParser(description="🚀 Multi-User Project Tracker CLI Suite")
    subparsers = parser.add_subparsers(dest="command", help="Operational Subcommands")

    # --- SUBCOMMAND: add-user ---
    p_add_user = subparsers.add_parser("add-user", help="Register a new system resource user.")
    p_add_user.add_argument("--name", required=True, help="Unique identity string for the user.")
    p_add_user.add_argument("--email", required=True, help="Contact email vector.")

    # --- SUBCOMMAND: list-users ---
    subparsers.add_parser("list-users", help="Enumerate all users.")

    # --- SUBCOMMAND: add-project ---
    p_add_proj = subparsers.add_parser("add-project", help="Create a project profile linked to a user.")
    p_add_proj.add_argument("--title", required=True, help="Unique identifier title.")
    p_add_proj.add_argument("--desc", default="No description provided.", help="Project context scope.")
    p_add_proj.add_argument("--due", default="2026-12-31", help="Target completion milestone target.")
    p_add_proj.add_argument("--user", required=True, help="Owner username constraint matching database entries.")

    # --- SUBCOMMAND: list-projects ---
    p_list_proj = subparsers.add_parser("list-projects", help="Enumerate monitored project records.")
    p_list_proj.add_argument("--user", help="Optional filter to scope view down to specific users.")

    # --- SUBCOMMAND: add-task ---
    p_add_task = subparsers.add_parser("add-task", help="Inject actionable tasks straight into a project.")
    p_add_task.add_argument("--project", required=True, help="Target project container matching system records.")
    p_add_task.add_argument("--title", required=True, help="Task description statement.")
    p_add_task.add_argument("--assignee", help="User tracking key handling this metric.")

    # --- SUBCOMMAND: complete-task ---
    p_comp_task = subparsers.add_parser("complete-task", help="Flag an active task instance as complete.")
    p_comp_task.add_argument("--id", required=True, help="Target Integer tracking code identity.")

    args = parser.parse_parse = parser.parse_args()
    
    # Load database state
    db = load_database()

    # --- ROUTING CRITERIA HANDLERS ---
    if args.command == "add-user":
        if args.name in db["users"]:
            console.print(f"[bold red] Mismatch Error:[/bold red] User '{args.name}' already logged.")
            sys.exit(1)
        db["users"][args.name] = User(args.name, args.email)
        save_database(db)
        console.print(f"[bold green]✔ Success:[/bold green] Account created for {args.name}.")

    elif args.command == "list-users":
        if not db["users"]:
            console.print("[yellow]Empty records pool.[/yellow]")
            return
        table = Table(title="System User Profiles")
        table.add_column("Account Key Name", style="cyan")
        table.add_column("Email Endpoint Address", style="magenta")
        for u in db["users"].values():
            table.add_row(u.name, u.email)
        console.print(table)

    elif args.command == "add-project":
        if args.user not in db["users"]:
            console.print(f"[bold red] Dependency Error:[/bold red] User profile '{args.user}' must exist before project instantiation.")
            sys.exit(1)
        if args.title in db["projects"]:
            console.print(f"[bold red] Conflict:[/bold red] Project '{args.title}' already exists.")
            sys.exit(1)
        db["projects"][args.title] = Project(args.title, args.desc, args.due, args.user)
        save_database(db)
        console.print(f"[bold green]✔ Success:[/bold green] Project '{args.title}' bound to user '{args.user}'.")

    elif args.command == "list-projects":
        target_projects = db["projects"].values()
        if args.user:
            target_projects = [p for p in target_projects if p.owner_name == args.user]
        
        if not target_projects:
            console.print("[yellow]No project allocations found matching request boundaries.[/yellow]")
            return
            
        table = Table(title="Project Matrix Board")
        table.add_column("Project Scope Title", style="green")
        table.add_column("Target Milestone", style="bold white")
        table.add_column("Owner Username", style="blue")
        for p in target_projects:
            table.add_row(p.title, p.due_date, p.owner_name)
        console.print(table)

    elif args.command == "add-task":
        if args.project not in db["projects"]:
            console.print(f"[bold red] Infrastructure Error:[/bold red] Project target '{args.project}' does not exist.")
            sys.exit(1)
        if args.assignee and args.assignee not in db["users"]:
            console.print(f"[bold red] Verification Error:[/bold red] Contributor '{args.assignee}' does not hold an active account.")
            sys.exit(1)
            
        next_id = str(len(db["tasks"]) + 1)
        db["tasks"][next_id] = Task(next_id, args.project, args.title, "Pending", args.assignee)
        save_database(db)
        console.print(f"[bold green]✔ Success:[/bold green] Task #{next_id} registered into target container '{args.project}'.")

    elif args.command == "complete-task":
        if args.id not in db["tasks"]:
            console.print(f"[bold red] Range Error:[/bold red] Task reference index '{args.id}' not tracking inside database.")
            sys.exit(1)
        db["tasks"][args.id].mark_complete()
        save_database(db)
        console.print(f"[bold green]✔ Success:[/bold green] Task #{args.id} updated to complete status.")
        
    else:
        parser.print_help()

if __name__ == "__main__":
    run_cli()
