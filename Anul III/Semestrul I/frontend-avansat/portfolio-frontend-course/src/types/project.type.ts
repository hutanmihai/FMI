export type Project = {
  id: string
  title: string
  description: string
  github_link?: string | null
  live_demo_link?: string | null
  youtube_link?: string | null
  technologies: string[]
}

export type Projects = Project[]
